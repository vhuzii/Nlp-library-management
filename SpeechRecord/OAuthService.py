import oauth2 as oauth
import urlparse

client_id = "HWhaO97bSHYSNloJ67lig"
secret = "okKwdxgll4kDz1u7XwitE7j9OiCmY9WN7IozKt204"

request_token_url = "https://www.goodreads.com/oauth/request_token"
authorize_url = "https://www.goodreads.com/oauth/authorize"
access_token_url = "https://www.goodreads.com/oauth/access_token"
base_url = "https://www.goodreads.com/"

#hardcoded for my machine, vova zamytu sobi sviy token, use getToken()
oauth_token_secret = 'N3DPTj26MrGUBBaf0RzOkJzCnnYz1zYVASTtlvsLFY'
oauth_token = 'ArcrtRTlOVL8kFMy1HoPA'

class OAuthService:

    def getToken(self):                     #use if using first time on machine, else -> hardcoded value
        consumer = oauth.Consumer(key=client_id,
                                  secret=secret)

        client = oauth.Client(consumer)

        response, content = client.request(unicode(request_token_url, "utf-8"), 'GET')

        request_token = dict(urlparse.parse_qsl(content))

        token = oauth.Token(request_token['oauth_token'],
                            request_token['oauth_token_secret'])
        client = oauth.Client(consumer, token)

        authorize_link = '%s?oauth_token=%s' % (authorize_url,
                                                request_token['oauth_token'])
        print ('Use to uathorize your MACHINA WROOOM ' + authorize_link)
        #
        accepted = 'n'
        while accepted.lower() == 'n':
            # you need to access the authorize_link via a browser,
            # and proceed to manually authorize the consumer
            accepted = raw_input('Accepted? (y/n) ')

        response, content = client.request(unicode(access_token_url, "utf-8"), 'POST')

        access_token = dict(urlparse.parse_qsl(content))
        return access_token

    def getClient(self):
        consumer = oauth.Consumer(key=client_id,secret=secret)
        token = oauth.Token(oauth_token, oauth_token_secret)

        client = oauth.Client(consumer, token)
        return client;
