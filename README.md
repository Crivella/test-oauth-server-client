# OAuth + django

This is a test on running the following:

- [django](https://github.com/django/django) + [django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit) to create a login server that supports OpenID Connect (OIDC)
- [django](https://github.com/django/django) + [django-allauth](https://github.com/pennersr/django-allauth) to use the login server for logging in users (via a grant-access flow)

* NOTES:

- `SESSION_COOKIE_PATH` in the settings is required for running the 2 django instances together on localhost: `django-allauth` uses the session to store the PKCE code verifier (generated when clicking on `continue` when selecting the server for authentication). If `SESSION_COOKIE_PATH` is not used, the session of the auth server will overwrite the one of the client (which will fail the auth because it won't have the PKCE code verifier anymore)