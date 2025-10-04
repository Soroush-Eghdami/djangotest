import datetime

class FileLogMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        
        
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response = self.get_response(request)
        status_code = response.status_code
        log = f"{ip} - {now} - {path} - {status_code}\n"
        with open('access.log', 'a', encoding='utf-8') as f:
            f.write(log)
        return response