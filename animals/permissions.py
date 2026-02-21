from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    อนุญาตให้อ่านได้ทุกคน (SAFE_METHODS)
    แต่ถ้าจะแก้/ลบ ต้องเป็น owner ของ object นั้นเท่านั้น
    """

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True
        # POST/PUT/PATCH/DELETE ต้องเป็นเจ้าของ
        return obj.owner == request.user
