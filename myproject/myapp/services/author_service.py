# services/author_service.py
from typing import List, Optional
from ..repositories.author_repository import AuthorRepository
from ..models import Author

class AuthorService:
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    def list_authors(self) -> List[Author]:
        return self.repo.get_all()

    def get_author(self, author_id: int) -> Optional[Author]:
        return self.repo.get_by_id(author_id)

    def create_author(self, name: str) -> Author:
        return self.repo.create(name=name)

    def update_author(self, author_id: int, **kwargs) -> Optional[Author]:
        print("update author")
        return self.repo.update(author_id, **kwargs)

    def delete_author(self, author_id: int) -> bool:
        return self.repo.delete(author_id)
