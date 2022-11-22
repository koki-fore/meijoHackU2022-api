from sqlalchemy.orm.session import Session

import app.models.challenge_category as challenge_category_model
import app.schemas.challenge_category as challenge_category_schema

def create_challenge_category(db: Session, challenge_category_create: challenge_category_schema.Challenge_category) -> challenge_category_model.Challenge_category:
    challenge_category=challenge_category_model.Challenge_category(**challenge_category_create.dict())
    db.add(challenge_category)
    db.commit()
    db.refresh(challenge_category)

    return challenge_category