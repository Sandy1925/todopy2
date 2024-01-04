from ninja import ModelSchema
from .models import Customer,Tasks

"""
Customer Input Schema for DTO
Author: Santhosh Kumar
Date Created: 14/12/2023
"""

class CustomerIn(ModelSchema):
    class Meta:
        model=Customer
        fields='__all__'

"""
Customer Output Schema as DTO
Author : Santhosh Kumar
Date Created: 14/12/2023
"""

class CustomerOut(ModelSchema):
    class Meta:
        model=Customer
        fields=['id','name','email']

"""
Customer Login Schema with email and password
Author: Santhosh kumar
Date Created: 20/12/2023
Date modified:
"""
class CustomerLogin(ModelSchema):
    class Meta:
        model=Customer
        fields=['email','password']


"""
Customer Login Output
Author: Santhosh Kumar
Date Created: 20/12/2023
Date Modified:
"""
class CustomerLogOut(ModelSchema):
    class Meta:
        model=Customer
        fields=['id','email','name']

"""
Task In Schema
Author: Santhosh Kumar
Date Created: 26/12/23
Date modified:
"""
class TaskIn(ModelSchema):
    class Meta:
        model=Tasks
        fields=['email','description']


"""
Task out Schema
Author: Santhosh Kumar
Date Created: 26/12/23
Date modified:
"""
class TaskOut(ModelSchema):
    class Meta:
        model=Tasks
        fields=['id','email','description','status','addedOn','completedOn','removedOn']


"""
Task Update Schema
Author: Santhosh Kumar
Date Created: 26/12/23
Date modified:
"""
class TaskUpdIn(ModelSchema):
    class Meta:
        model=Tasks
        fields=['description','status']
