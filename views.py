from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TemperaturePrediction

@csrf_exempt
def predict_temperature(request):
    if request.method == 'POST':
        apparent_temperature = request.POST.get('apparent_temperature')
        if not apparent_temperature:
            return JsonResponse({'error': 'Apparent temperature is required.'}, status=400)
        
        # Perform temperature prediction logic here (replace this with your actual prediction code)
        predicted_temperature = float(apparent_temperature) * 1.5
        
        # Save the prediction to the database
        prediction = TemperaturePrediction.objects.create(
            apparent_temperature=apparent_temperature,
            predicted_temperature=predicted_temperature
        )

        return JsonResponse({'predicted_temperature': predicted_temperature}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
