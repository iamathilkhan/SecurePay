from speechbrain.pretrained import SpeakerRecognition

verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec"
)

def verify_voice(v1, v2):
    score, prediction = verification.verify_files(
        v1,
        v2
    )

    return score, prediction

    print("Score:", score)
    print("Is same person:", prediction)
