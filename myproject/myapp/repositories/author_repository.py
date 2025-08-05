# repositories/author_repository.py
from typing import List, Optional
from ..models import Author
from django.db.models.fields.related import ManyToManyField, ForeignKey

class AuthorRepository:
    """Repository class for Author model."""

    def get_all(self) -> List[Author]:
        return list(Author.objects.all())

    def get_by_id(self, author_id: int) -> Optional[Author]:
        try:
            return Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return None

    def create(self, name: str) -> Author:
        author = Author(name=name)
        author.save()
        return author

    def update(self, author_id: int, **kwargs) -> Optional[Author]:
        author = self.get_by_id(author_id)
        if author is None:
            return None

        m2m_updates = {}

        for key, value in kwargs.items():
            try:
                field = Author._meta.get_field(key)
                print("field",field)
            except Exception:
                # Skip invalid fields
                continue

            if isinstance(field, ManyToManyField):
                # Defer M2M field update until after save
                m2m_updates[key] = value
            elif field.auto_created:
                # Skip reverse relations (e.g., books_set)
                continue
            else:
                setattr(author, key, value)

        author.save()

        # Set ManyToMany fields after save
        for key, value in m2m_updates.items():
            getattr(author, key).set(value)

        return author

    def delete(self, author_id: int) -> bool:
        author = self.get_by_id(author_id)
        if author is None:
            return False
        author.delete()
        return True
