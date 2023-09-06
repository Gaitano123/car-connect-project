import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Garage, Owner, Car

engine = create_engine('sqlite:///project.db')
Session = sessionmaker(bind=engine)
session = Session()


@click.command()
def list_garage():
    click.secho("LIST OF GARAGES",fg='blue' )
    garages = session.query(Garage).all()
    for garage in garages:
        click.echo(f"{garage.id}: {garage.name}")
   
   
        
@click.command()
@click.option('--name', '-n', prompt='Enter the new garage name')
def add_garage(name):
    new_garage = Garage(name=name)
    session.add(new_garage)
    session.commit()
    click.secho(f'Garage {name} is sucessfully added!', fg='green')
      
      
        
@click.command()
@click.option('--name', '-sg', prompt='Search for garage')
def search_garage(name):
    garage = session.query(Garage).filter(Garage.name == name).first()
    if garage:
        click.secho(f'found {garage.id}: {garage.name}', fg='blue')
    else:
        click.secho(f'Garage {name} not found!', fg='yellow')
        


@click.command()
@click.option('--name', '-n', prompt='Enter name to be updated')
@click.option('--new-name', '-nn', prompt='Enter the new name')
def update_garage(name, new_name):
    update_garage = session.query(Garage).filter(Garage.name == name).first()
    if update_garage:
        session.query(Garage).filter(Garage.id == update_garage.id).update({
            Garage.name: new_name
        })
        session.commit()
        click.secho('Garage updated successfully!', fg='blue') 
    else:
        click.secho(f'Garage {name} does not exist!', fg='yellow')
        
    
  
@click.command()
@click.option('--name', '-dn', prompt='Enter the Garage name to be deleted')
def delete_garage(name):
    to_delete = session.query(Garage).filter(Garage.name == name).first()
    if to_delete:
        session.delete(to_delete)
        session.commit()
        click.secho('Garage deleted successfully!', fg='blue')
    else:
        click.secho(f'Garage {name} does not exist!', fg='yellow')


          
@click.command()
def list_owners():
    click.secho("LIST OF OWNERS",fg='blue' )
    owners = session.query(Owner).all()
    for owner in owners:
        click.echo(f"{owner.id}: {owner.name}")



@click.command()
@click.option('--name', '-n', prompt='Enter new owner name')
def add_owner(name):
    new_owner = Owner(name=name)
    session.add(new_owner)
    session.commit()
    click.secho(f'Owner {name} successfully added!', fg='green')
    
    
    
@click.command()
@click.option('--name', '-sn', prompt='Search for owner')
def search_owner(name):
    found = session.query(Owner).filter(Owner.name == name).first()
    if found:
        click.secho(f'Found Owner {found.id}: {found.name}', fg='blue')
    else:
        click.secho(f'Owner {name} not found!', fg='yellow')


@click.command()
@click.option('--name', '-on', prompt="Enter name to be updated")
@click.option('--new-name', '-nn', prompt="Enter name")
def update_owner(name, new_name):
    update = session.query(Owner).filter(Owner.name == name).first()
    if update:
        update.name = new_name
        session.commit()
        click.secho('Owner updated successfully!', fg='blue')
    else:
        click.secho('Owner not found!', fg='yellow')


@click.command()
@click.option('--name', '-dn', prompt="Enter Owner Name")
def delete_owner(name):
    to_delete = session.query(Owner).filter(Owner.name == name).first()
    if to_delete:
        session.delete(to_delete)
        session.commit()
        click.secho('Owner sucessfully deleted!',fg='blue')
    else:
        click.secho(f'Owner {name} not found!', fg='yellow')


@click.command()
def list_cars():
    cars = session.query(Car).all()
    click.secho('LIST OF CARS', fg='blue')
    for car in cars:
        click.echo(f'{car.id}: {car.make} {car.model}')
        
@click.command()
@click.option('--make', '-mk', prompt='Enter make')
@click.option('--model', '-md', prompt='Enter model')
@click.option('--year', '-y', prompt='Enter year')
@click.option('--owner-id', '-oi', prompt='Enter owner id')
@click.option('--garage-id', '-gi', prompt='Enter garage id')
def add_car(make, model, year, owner_id, garage_id):
    car= Car(make= make, model=model, year=year, owner_id=owner_id, garage_id=garage_id)
    session.add(car)
    session.commit()
    click.secho('car has been added successfully!', fg='blue')

if __name__ == "__main__":
    list_garage()
    add_garage()
    search_garage()
    update_garage()
    delete_garage()
    list_owners()
    add_owner()
    search_owner()
    update_owner()
    delete_owner()
    list_cars()
    add_car()
