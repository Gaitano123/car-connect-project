import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Garage, Owner, Car



engine = create_engine('sqlite:///project.db')
Session = sessionmaker(bind=engine)
session = Session()



@click.group()
def cli():
    pass



@cli.command()
def list_garage():
    
    """LIST ALL THE GARAGES IN THE TABLE"""
    
    click.secho("LIST OF GARAGES",fg='blue' )
    garages = session.query(Garage).all()
    for garage in garages:
        click.echo(f"{garage.id}: {garage.name} in {garage.location}.")
   
   
        
@cli.command()
@click.option('--name', '-n', prompt='Enter garage name')
@click.option('--location', '-l', prompt='Enter location')
def add_garage(name, location):
    
    """ADD'S A NEW GARAGE TO THE DATABASE"""
    
    new_garage = Garage(name=name, location=location)
    session.add(new_garage)
    session.commit()
    click.secho(f'Garage {new_garage.name} located at {new_garage.location} is sucessfully added!', fg='green')
      
      
        
@cli.command()
@click.option('--name', '-sg', prompt='Search for garage')
def search_garage(name):
    
    """SEARCH FOR A GARAGE BY THE NAME"""
    
    garage = session.query(Garage).filter(Garage.name == name).first()
    if garage:
        click.secho(f'found {garage.id}: {garage.name} in {garage.location}', fg='blue')
    else:
        click.secho(f'Garage {name} not found!', fg='yellow')
        
        
        
@cli.command()
@click.option('--location', '-l', prompt='Enter location')
def search_garage_location(location):
    
    """SEARCH FOR GARAGES IN DESIRED LOCATION"""
    
    garages = session.query(Garage).filter(Garage.location == location).all()
    if garages:
        click.secho(f'LIST OF GARAGES FOUND IN: {location}', fg='blue')
        for garage in garages:
            click.echo(f'Garage {garage.id}: {garage.name}')
    else:
        click.secho(f'Garages located in {location} not found!', fg='yellow')

        

@cli.command()
@click.option('--id', '-id', prompt='Enter id to be updated')
@click.option('--new-name', '-nn', prompt='Enter the new name')
def update_garage_name(id, new_name):
    
    """UPDATE NAME OF A GARAGE USING IT'S ID"""
    
    update_garage = session.query(Garage).filter(Garage.id == id).first()
    if update_garage:
        session.query(Garage).filter(Garage.id == update_garage.id).update({
            Garage.name: new_name
        })
        session.commit()
        click.secho('Garage updated successfully!', fg='blue') 
    else:
        click.secho(f'Garage with id: {id} does not exist!', fg='yellow')
        
        
        
@cli.command()
@click.option('--id', '-id', prompt='Enter garage id')
def search_garage_car(id):
    
    """SEARCH FOR CARS THAT ARE SERVICED BY A CERTAIN GARAGAE"""
    
    garage = session.query(Garage).filter(Garage.id == id).first()
    if garage:
        click.secho(f'LIST OF CARS SERVICED AT: {garage.name}', fg='blue')
        cars = session.query(Car).filter(Car.garage_id == garage.id).all()
        for car in cars:
            owner = session.query(Owner).filter(Owner.id == Car.id).first()
            click.echo(f'{car.id}: Make: {car.make}, Model: {car.model}, Year: {car.year} owned by {owner.name}')
    else:
        click.secho(f'Garage with ID: {id} not found!', fg='yellow')



@cli.command()
@click.option('--id', '-dn', prompt='Enter the Garage id to be deleted')
def delete_garage(id):
    
    """DELETES A GARAGE FROM THE DATABASE"""
    
    to_delete = session.query(Garage).filter(Garage.id == id).first()
    if to_delete:
        session.delete(to_delete)
        session.commit()
        click.secho('Garage deleted successfully!', fg='blue')
    else:
        click.secho(f'Garage with id: {id} does not exist!', fg='yellow')



@cli.command()
def list_owners():
    
    """LIST ALL THE OWNERS"""
    
    click.secho("LIST OF OWNERS",fg='blue' )
    owners = session.query(Owner).all()
    for owner in owners:
        click.echo(f"{owner.id}: {owner.name}")



@cli.command()
@click.option('--name', '-n', prompt='Enter new owner name')
def add_owner(name):
    
    """ADD A NEW OWNER """
    
    new_owner = Owner(name=name)
    session.add(new_owner)
    session.commit()
    click.secho(f'Owner {name} successfully added!', fg='green')

    
    
@cli.command()
@click.option('--name', '-sn', prompt='Search for owner')
def search_owner(name):
    
    """SEARCH FOR AN OWNER WITH SPECIFIC NAME"""
    
    found = session.query(Owner).filter(Owner.name == name).first()
    if found:
        click.secho(f'Found Owner {found.id}: {found.name}', fg='blue')
    else:
        click.secho(f'Owner {name} not found!', fg='yellow')



@cli.command()
@click.option('--id', '-on', prompt="Enter id")
@click.option('--new-name', '-nn', prompt="Enter new name")
def update_owner(id, new_name):
    
    """UPDATE ANOWNER'S NAME"""
    
    update = session.query(Owner).filter(Owner.id == id).first()
    if update:
        update.name = new_name
        session.commit()
        click.secho('Owner updated successfully!', fg='blue')
    else:
        click.secho('Owner not found!', fg='yellow')
        
        
        
@cli.command()
@click.option('--id', '-id', prompt='Enter owner id')
def search_owner_car(id):
    
    """SEARCH FOR CARS THAT BELONG TO AN INDIVIDUAL OWNER"""
    
    owner = session.query(Owner).filter(Owner.id == id).first()
    if owner:
        click.secho(f'LIST OF CARS OWNED BY: {owner.name}', fg='blue')
        cars = session.query(Car).filter(Car.owner_id == owner.id).all()
        for car in cars:
            click.echo(f'{car.id}: Make: {car.make}, Model: {car.model}, Year: {car.year}')
    else:
        click.secho(f'Owner with ID: {id} not found!', fg='yellow')
        


@cli.command()
@click.option('--id', '-id', prompt="Enter Owner id")
def delete_owner(id):
    
    """DELETE OWNER'S DETAILS"""
    
    to_delete = session.query(Owner).filter(Owner.id == id).first()
    if to_delete:
        session.delete(to_delete)
        session.commit()
        click.secho('Owner sucessfully deleted!',fg='blue')
    else:
        click.secho(f'Owner with id: {id} not found!', fg='yellow')



@cli.command()
def list_cars():
    
    """LIST ALL CARS"""
    
    cars = session.query(Car).all()
    click.secho('LIST OF CARS', fg='blue')
    for car in cars:
        click.echo(f'{car.id}: {car.make} {car.model}')
  
  
        
@cli.command()
@click.option('--make', '-mk', prompt='Enter make')
@click.option('--model', '-md', prompt='Enter model')
@click.option('--year', '-y', prompt='Enter year')
@click.option('--owner-id', '-oi', prompt='Enter owner id')
@click.option('--garage-id', '-gi', prompt='Enter garage id')
def add_car(make, model, year, owner_id, garage_id):
    
    """ADD A NEW CAR"""
    
    car= Car(make= make, model=model, year=year, owner_id=owner_id, garage_id=garage_id)
    session.add(car)
    session.commit()
    click.secho('car has been added successfully!', fg='blue')



@cli.command()
@click.option('--id', '-id', prompt='Enter the car id')
@click.option('--owner-id', '-oi', prompt='Enter the new owner id')
def update_car_owner(id, owner_id):
    
    """UPDATE CAR OWNER"""
    
    update = session.query(Car).filter(Car.id == id).first()
    if update:
        update.owner_id = owner_id
        session.commit()
        click.secho('car owner has been updated successfully!', fg='blue')
    else:
        click.secho(f'Car with the id: {id} is not found!', fg='yellow')



@cli.command()
@click.option('--id', '-id', prompt='Enter the car id', type=int)
@click.option('--garage-id', '-gi', prompt='Enter the new garage id', type=int)
def update_car_garage(id, garage_id):
    
    """UPDATE GARAGE SERVICING THE CAR"""
    
    update= session.query(Car).filter(Car.id == id).first()
    if update:
        update.garage_id = garage_id
        session.commit()
        click.secho('car garage has been updated successfully!', fg='blue')
    else:
        click.secho(f'Car with the id: {id} is not found!', fg='yellow')
        
        

@cli.command()
@click.option('--id', '-id', prompt='Enter the id of the car')
def delete_car(id):
    
    """DELETE A CAR"""
    
    to_delete = session.query(Car).filter(Car.id == id).first()
    if to_delete:
        session.delete(to_delete)
        session.commit()
        click.secho('Car deleted sucessfully!',fg='blue')
    else:
        click.secho(f'Car with id: {id} not found!', fg='yellow')



@cli.command()
def list_all():
    
    """LIST ALL CARS INCLUDING THEIR OWNER AND GARAGE DETAILS"""
    
    cars = session.query(Car).all()
    click.secho('LIST OF CARS', fg='blue')
    for car in cars:
        owner = session.query(Owner).filter(Owner.id == car.owner_id).first()
        garage = session.query(Garage).filter(Garage.id == car.garage_id).first()
        if owner and garage:
            click.echo(
                f'{car.id}: Make: {car.make}, Model: {car.model}, Year: {car.year}, Owner: {owner.name}, Garage: {garage.name}'
            )
        else:
            click.echo(
                f'{car.id}: Make: {car.make}, Model: {car.model}, Year: {car.year}, Owner ID: {car.owner_id}, Garage ID: {car.garage_id}'
            )


    
if __name__ == "__main__":
    cli()
