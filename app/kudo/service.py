from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import KudoSchema

class Service(object):
    def __init__(self, user_id, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client
        self.user_id = user_id

        if not user_id:
            raise Exception("No user found!")
    
    def find_all_kudos(self):
        kudos = self.repo_client.find_all({'user_id': self.user_id})
        return [self.dump(kudo) for kudo in kudos]

    def find_kudo(self, repo_id):
        kudo = self.repo_client.find({'user_id': self.user_id, 'repo_id': repo_id})
        return self.dump(kudo)