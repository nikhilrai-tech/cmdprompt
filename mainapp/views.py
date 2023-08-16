import subprocess
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
import re

@api_view(['POST'])
def execute_command(request):
    if request.method == 'POST':
        command = request.data.get('command', '')
        output = run_command(command)
        return Response({'output': output})

    return Response({'output': ''})

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8').strip()  # Remove leading/trailing whitespace

    if error:
        return f"Error: {error.decode('utf-8')}"


    with open('output.txt', 'w+') as output_file:
        output_file.write(f"Command: {command}\n")
        output_file.write(f"Output:\n{output}\n")
        output_file.write('-' * 50 + '\n')

    return output

@api_view(['GET'])
def download_output(request):
    file_path = r'C:\Users\Nikhil Rai\Downloads\ghost\ghost\server\output.txt'

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = Response(file.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=output.txt'
            return response

    else:
        return Response('Output file not found.')
