from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import permissions
from project_settings.tasks import debug_task

class AllowedToFetch(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.is_allowed_to_fetch:
                return True
            else:
                return False
        except Exception as e:
                return False


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated & AllowedToFetch])
def get_data(request):
    debug_task.delay(
        dbhost = request.data['dataurl'],
        dbname = request.data['dbname'],
        username = request.data['username'],
        passwd = request.data['password'],
        table = "links",
        user_id = request.user.id
    )
    return Response({"message": "Successfull"},status=200)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated & AllowedToFetch])
def get_recent_file(request):
    return Response({
            "updated_at":request.user.updated_at,
            "data_file_name_url": f"http://localhost:8028/media/csv_files/{request.user.data_file_name}"
        },status=200)