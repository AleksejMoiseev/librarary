from wsgiref.simple_server import make_server

import falcon

from algoritmika.core.exceptions import BaseNotFoundException, NotFoundEntity
from algoritmika.exception import NotStatusExceptioms
from algoritmika.library.exceptions import InccorectedRequestException
from algoritmika.library.views import (
    LibraryCreateView, UsersLibraryView, BooksLibraryView
)
from algoritmika.middleware import (
    JSONTranslator, JWTUserAuthView,
)
from algoritmika.notes.exceptions import NotesNotFoundEntity
from algoritmika.notes.views import NotesListCreateView, NotesRetrieveView
from algoritmika.users.exceptions import UserNotFoundException
from algoritmika.users.views import (
    UserListCreateController, UserRetrieveController,
    UserRetrieveView, UserListCreateView
)
from algoritmika.views import (
    ThingsResource, UserController, UsersController,
    BookBaseViews, IssueRetrieveView, IssueListCreateView, SortedIssue,
    TackNumberFour, FilterBaseView,
)

from algoritmika.issues.views import IssuesListCreateView, IssuesRetrieveView
from algoritmika.issues.exceptions import IssuesNotFoundEntity

middleware = [
    JSONTranslator(),
    #JWTUserAuthMiddleware(),

]

app = falcon.App(middleware=middleware)
app.add_error_handler(NotStatusExceptioms)
app.add_error_handler(BaseNotFoundException)
app.add_error_handler(UserNotFoundException)
app.add_error_handler(NotFoundEntity)
app.add_error_handler(InccorectedRequestException)
app.add_error_handler(NotesNotFoundEntity)
app.add_error_handler(IssuesNotFoundEntity)

# Resources are represented by long-lived class instances
things = ThingsResource()
user_controller = UserController()
users_controller = UsersController()
books_controller = BookBaseViews()


# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/users/', UserListCreateController())
app.add_route('/users-1/', UserListCreateView())
app.add_route('/users/{user_id}', UserRetrieveController())
app.add_route('/users-1/{user_id}', UserRetrieveView())
app.add_route('/books/{book_id}', books_controller)
app.add_route('/notes/{pk}', NotesRetrieveView())
app.add_route('/notes/', NotesListCreateView())
app.add_route('/issues/', IssuesListCreateView())
app.add_route('/issues/{pk}', IssuesRetrieveView())
app.add_route('/sorted-issues/', SortedIssue())
app.add_route('/status/{status}', TackNumberFour())
app.add_route('/filters/', FilterBaseView())
app.add_route('/login/', JWTUserAuthView())

"""Library"""

app.add_route('/bookss/{action}', LibraryCreateView())
app.add_route('/bookss/', BooksLibraryView())
app.add_route('/userss/', UsersLibraryView())

if __name__ == '__main__':
    with make_server(host="127.0.0.1", port=8003, app=app) as httpd:
        httpd.serve_forever()

