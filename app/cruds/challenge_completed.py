from sqlalchemy.orm.session import Session

import app.models.challenge_completed as challenge_completed_model
import app.schemas.challenges_completed as challenge_completed_schema

def create_challenge_completed(db: Session, challenge_completed_create: challenge_completed_schema.Challenge_completedCreate) -> challenge_completed_model.Challenge_completed:
    challenge_completed=challenge_completed_model.Challenge_completed(**challenge_completed_create.dict())
    db.add(challenge_completed)
    db.commit()
    db.refresh(challenge_completed)

    return challenge_completed