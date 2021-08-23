# Here we are going to implement AWS cognito user pool using boto3

import boto3
from pprint import pprint


class CognitoOperation:
    # client object
    client = boto3.client('cognito-idp')
    email = 'vishvajit.rao@in.nuagebiz.tech'
    password = 'Vishvajitrao12!'
    client_id = '69t9k20se1t789tf4aimp44mb1'
    pool_id = 'us-east-1_b73sKgx8V'

    @classmethod
    def user_signup(cls, username):
        response = {"success": False, "user_exists": False, "server_error": False}
        # user sign up
        try:
            cls.client.sign_up(
                ClientId=cls.client_id,
                Username=username,
                Password=cls.password,
                UserAttributes=[
                    {"Name": "email", "Value": username},
                ],
                ValidationData=[{"Name": "email", "Value": username}],
                ClientMetadata={"emailId": username},
            )
            response.update({"success": True})
        except cls.client.exceptions.UsernameExistsException:
            response.update({"success": False})

        return response

    # confirm user sign up
    @classmethod
    def enable_user(cls, username, confirmation_code):

        response = {
            "success": False,
            "user_not_found": False,
            "invalid_code": False,
            "not_authorized": False,
            "server_error": False,
            "code_expire": False,
        }

        try:

            cls.client.confirm_sign_up(
                ClientId=cls.client_id, Username=username, ConfirmationCode=confirmation_code
            )

            response.update({"success": True})

        # User is not exists
        except cls.client.exceptions.UserNotFoundException:
            response.update({"user_not_found": True})

        # Confirmation code is invalid
        except cls.client.exceptions.CodeMismatchException:
            response.update({"invalid_code": True})

        # User haven't activate the account yet
        except cls.client.exceptions.NotAuthorizedException:
            response.update({"not_authorized": True})

        # When the code expires
        except cls.client.exceptions.ExpiredCodeException:
            response.update({"code_expire": True})

        except Exception as e:
            response.update({"server_error": True, "message": str(e)})

        return response

    @classmethod
    def client_re_send_verification_code(cls, username):
        """
        This method will re send the account confirmation code
        """
        response = {"success": False, "user_not_found": False, "server_error": False}

        try:

            cls.client.resend_confirmation_code(
                ClientId=cls.client_id, Username=username, ClientMetadata={"emailId": username},
            )

            response.update({"success": True})

        # User is not exists
        except cls.client.exceptions.UserNotFoundException:
            response.update({"user_not_found": True})

        except Exception as e:
            response.update({"server_error": True, "message": str(e)})

        print("CognitoOperations.client_re_send_verification_code - ", response)
        return response

    # user sign in
    @classmethod
    def client_login(cls, username, password):
        """
        This method will login and provide the token information
        """

        response = {
            "success": False,
            "user_not_found": False,
            "user_not_confirmed": False,
            "not_authorized": False,
            "server_error": False,
        }

        try:

            resp = cls.client.initiate_auth(
                ClientId=cls.client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={"PASSWORD": password, "USERNAME": username},
            )

            response.update({"user_data": resp, "success": True})

        # User is not exists
        except cls.client.exceptions.UserNotFoundException:
            response.update({"user_not_found": True})

        # Wrong email or password
        except cls.client.exceptions.NotAuthorizedException:
            response.update({"not_authorized": True})

        # User haven't activate the account yet
        except cls.client.exceptions.UserNotConfirmedException:
            response.update({"user_not_confirmed": True})

        except Exception as e:
            response.update({"server_error": True, "message": str(e)})

        return response

    @classmethod
    def list_user(cls):
        """
        This method will login and provide the token information
        """

        response = {
            "success": False,
        }

        try:

            resp = cls.client.list_users(
                UserPoolId=cls.pool_id,
                AttributesToGet=[
                    'email',
                ]
            )

            response.update({"user_data": resp, "success": True})

        # User is not exists
        except cls.client.exceptions.InvalidParameterException:
            response.update({"invalid_parameter_exception": True})

        # Wrong email or password
        except cls.client.exceptions.ResourceNotFoundException:
            response.update({"ResourceNotFoundException": True})

        # User haven't activate the account yet
        except cls.client.exceptions.UserNotConfirmedException:
            response.update({"UserNotConfirmedException": True})

        except Exception as e:
            response.update({"server_error": True, "message": str(e)})

        return response

# user1 = CognitoOperation.user_signup('vishvajit.rao@in.nuagebiz.tech')
# print(user1)
#
# confirm_signup = CognitoOperation.enable_user('vishvajit.rao@in.nuagebiz.tech', '372390')
# print(confirm_signup)

# resend_code = CognitoOperation.client_re_send_verification_code('vishvajit.rao@in.nuagebiz.tech')
# print(resend_code)

# login user
# login = CognitoOperation.client_login('vishvajit.rao@in.nuagebiz.tech', 'Vishvajitrao12!')
# print(login)

# list of cognito users
login = CognitoOperation.list_user()
pprint(login)


