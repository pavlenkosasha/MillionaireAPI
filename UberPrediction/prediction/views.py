import os
import joblib
import pandas as pd

from django.conf import settings
from django.shortcuts import render


MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "prediction",
    "uber_model.pkl"
)

model = joblib.load(MODEL_PATH)


def home(request):
    prediction = None

    if request.method == "POST":
        hour = int(request.POST["hour"])
        day = int(request.POST["day"])
        day_of_week = request.POST["day_of_week"]

        data = pd.DataFrame({
            "Hour": [hour],
            "Day": [day],
            "DayOfWeek": [day_of_week]
        })

        prediction = model.predict(data)[0]
        prediction = round(prediction)

    return render(
        request,
        "prediction/index.html",
        {"prediction": prediction}
    )