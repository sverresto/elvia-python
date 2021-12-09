from elvia import Elvia
import json
import os

token = os.environ.get("ELVIA_TOKEN")

elvia = Elvia(token)
meter_value_client = elvia.meter_value()

print(
    json.dumps(
        meter_value_client.get_meter_values(
            {
                "start_time": "2021-12-08T01:00:00",
                "end_time": "2021-12-08T02:00:00",
                "include_production": True,
            }
        )
    )
)

max_hours = meter_value_client.get_max_hours(
    {
        "calculate_time": "2021-12-08T01:00:00",
        "include_production": True,
    }
)

print(json.dumps(max_hours["meteringpoints"]))