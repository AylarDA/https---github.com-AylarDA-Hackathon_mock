from sqlalchemy.orm import Session, joinedload
from models import Images, Users, Application
from upload_depends import upload_image, delete_uploaded_image
from sqlalchemy import or_, and_, func


def create_image(id, file, db: Session):
    uploaded_img_name = upload_image('profile', file)
    new_add = Images(
        img = uploaded_img_name
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_image(db:Session):
    result = db.query(Images).all()
    return result


def delete_image(id, db: Session):
    image = db.query(Images).filter(Images.id == id).first()
    if image.img:
        delete_uploaded_image(image_name=image.img)
        db.query(Images).filter(Images.id == id) \
            .delete(synchronize_session=False)
        db.commit()
    return True


def signUp(req, db: Session):
    if req.name and req.city and req.adress and req.number and req.password == '' or \
        len(req.password) < 8 or \
        ' ' in req.name and ' ' in req.adress and ' ' in req.number and ' ' in req.password:
        return -1 
    user = db.query(Users).filter(
        or_(
            Users.password == req.password,
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
                Users.number == req.number,
                Users.password == req.password
            ),
            Users.password == req.password
        )
    ).first()
    if user:
        return True
    
    
def read_users(db: Session):
    return db.query(Users).all()


def create_application(req, db:Session):
    new_add = Application(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_application(status, db:Session):
    result = db.query(Application)
    if status:
        result = result.filter(Application.status == status)
    return result.all()


def read_current_application(id, db:Session):
    result = db.query(Application).filter(Application.id == id).first()
    return result