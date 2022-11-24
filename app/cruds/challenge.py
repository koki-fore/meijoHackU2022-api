from sqlalchemy.orm.session import Session

from typing import List
import app.models.challenge as challenge_model
import app.schemas.challenge as challenge_schema

def create_challenge(db: Session, challenge_create: challenge_schema.ChallengeCreate) -> challenge_model.Challenge:
    challenge=challenge_model.Challenge(**challenge_create.dict())
    db.add(challenge)
    db.commit()
    db.refresh(challenge)

    return challenge

def get_all_challenges(db: Session) -> List[challenge_model.Challenge]:
    challenges = db.query(challenge_model.Challenge).all()
    return challenges
