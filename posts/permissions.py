from rest_framework import permissions 

class IsAuthorOrReadOnly(permissions.BasePermission):

	def has_permission(self, request, view):
		# only authenticated users can see this list
		if request.user.is_authenticated:
			return True 
		return False

	def has_object_permission(self, request, view, obj):
		# read permisiions are allowe for any request, so we'll always allow
		# GET, HEAD, OPTIONS request
		if request.method in permissions.SAFE_METHODS:
			return True 

		# write parmissions are only allowed to the author of the post
		return obj.author == request.user