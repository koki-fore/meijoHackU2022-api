from sqlalchemy.orm.session import Session

import app.models.challenge as challenge_model
import app.schemas.challenge as challenge_schema

def create_challenge(db: Session, challenge_create: challenge_schema.ChallengeCreate) -> challenge_model.Challenge:
    challenge=challenge_model.Challenge(**challenge_create.dict())
    db.add(challenge)
    db.commit()
    db.refresh(challenge)

    return challenge