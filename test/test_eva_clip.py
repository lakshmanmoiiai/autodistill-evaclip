from src.eva_clip_model import EvaCLIP
from autodistill.detection import CaptionOntology


def test_eval_clip_classification():
    eva_clip = EvaCLIP(ontology=CaptionOntology(
        {
            "person": "person",
            "a forklift": "forklift"
        }
    ))
    assert eva_clip is not None
