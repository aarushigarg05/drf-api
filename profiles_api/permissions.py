from rest_framework import permissions

# we want users to views any profile they want but edit only their own
class UpdateOwnProfile(permissions.BasePermission): 
    # allows user to only edit their profile
    def has_object_permission(self,request,view,obj):
        # get will allow view, so is safe but update is not safe. so we check if it is in safe or unsafe category
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # if not in safe, we will check if object they are updating matches their authenticated profile.
        # we will match their id
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    # allow users to update only their status

     def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id

    
