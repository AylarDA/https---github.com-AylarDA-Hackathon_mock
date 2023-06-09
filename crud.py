from sqlalchemy.orm import Session, joinedload
from models import Category, Product, Images, About, Users
from upload_depends import upload_image
from sqlalchemy import or_, and_, func


def create_category(req, db:Session):
    new_add = Category(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_category(db:Session):
    result = db.query(Category).options(joinedload(Category.product)).all()
    return result


def read_current_category(id, db:Session):
    result = db.query(
        Category.id,
        Category.name,
        Product.name.label('product_name')
    ).join(Category, Category.id == Product.category_id).filter(Category.id == id).all()
    return result


def create_product(req, db:Session):
    new_add = Product(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add
    

def read_product(db:Session):
    result = db.query(
        Product.id,
        Product.name,
        Category.name.label('category_name')
    ).join(Category, Category.id == Product.category_id).all()
    return result


def create_image(id, file, db: Session):
    uploaded_img_name = upload_image('profile', file)
    new_add = Images(
        img = uploaded_img_name,
        product_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def create_about(req, db:Session):
    new_add = About(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_about(db:Session):
    result = db.query(About).all()
    return result


def signUp(req, db: Session):
    user = db.query(Users).filter(
        or_(
            Users.email == req.email,
            Users.username == req.username
        )
    ).first()
    if user:
        return False
    new_add = Users(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True


def signIn(req, db: Session):
    user = db.query(Users).filter(
        and_(
            or_(
                Users.email == req.email,
                Users.username == req.email
            ),
            Users.password == req.password
        )
    ).first()
    if user:
        return True
    
    
def read_users(db: Session):
    return db.query(Users.id, Users.email, Users.username).all()


# def search(q, db:Session):
#     result = db.query(Product)\
#         .filter(
#             or_(
#                 func.lower(Product.name).like(f'%{q}%'),
#             )  
#         ).all()
#     return result