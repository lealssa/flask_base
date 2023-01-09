from bson import ObjectId

from models.user import (
    UserEmailRecoverViewModel, 
    UserPasswordResetViewModel, 
    UserRegistrationViewModel, 
    UserLoginViewModel,
    UserBase,
    UserSec,
    UserLogin
    )

from models.error import (
    UserNotFoundError, 
    IvalidPasswordResetTokenError, 
    UsernameOrPasswordInvalidError,
    UserExistsError
    )

from repository.user import UserRepository

from services.security import create_password_hash, check_password_hash

from flask_login import login_user

class UserDomain:

    @staticmethod
    def SendPasswordResetIdEmail(user_email_recover: UserEmailRecoverViewModel) -> any:
        """ 
        Search user by email and send recover link.
        """

        email = 'myemail@maydomain.com'

        if user_email_recover.email != email:
            raise UserNotFoundError()

    @staticmethod
    def ResetUserPassword(user_password_reset: UserPasswordResetViewModel):
        """Reset user password by token"""

        if user_password_reset.token != '1234':
            raise IvalidPasswordResetTokenError()

    @staticmethod
    def RegisterUser(user_register: UserRegistrationViewModel):
        """Register an user"""  

        user_repo = UserRepository(UserBase)              

        has_user = user_repo.filter_by(email=user_register.email).first()

        if has_user:
            raise UserExistsError()

        user_register.id = ObjectId()
        user_register.password = create_password_hash(user_register.password)
        user_register.login = user_register.email
              
        user_repo.add(user_register)

    @staticmethod
    def ValidateUserCredentials(user_login: UserLoginViewModel) -> UserLogin:
        """Validate user and password"""

        user_repo = UserRepository(UserSec)    

        has_user = user_repo.filter_by(email=user_login.login).first()

        if not has_user:
            raise UserNotFoundError()      

        if not check_password_hash(user_login.password, has_user.password):
            raise UsernameOrPasswordInvalidError()            

        user_login = UserLogin(**has_user.dict())

        return user_login        