# -*- coding: utf-8 -*-
"""db/collection.py
By David J. Thomas, thePortus.com, dave.a.base@gmail.com

Model for a single collection with the USF Dime Novel collections. Contains
the metadata for the collection, as well the URL path where collection items
may be scraped. Collections may have multiple publishers or subjects, so
their simple models are included here, as well as the many-to-many tables.
"""
import peewee as sql

from .base_model import BaseModel


class Collection(BaseModel):
    name = sql.CharField()
    # The USF Library Digital Collection's ID number
    cid = sql.CharField()
    publication_date = sql.DateTimeField()
    formatting = sql.CharField()
    source_institution = sql.CharField()

    @property
    def publishers(self):
        """
        Gets all publishers of the collection via the many-to-many table
        """
        return Publisher.select().join(
            PublisherInCollection
        ).join(
            Collection
        ).where(
            Collection.cid == self.cid
        )

    @property
    def subjects(self):
        """
        Gets all subjects in the collection via the many-to-many table
        """
        return Subject.select().join(
            SubjectInCollection
        ).join(
            Collection
        ).where(
            Collection.cid == self.cid
        )


class Publisher(BaseModel):
    name = sql.CharField()

    @property
    def collections(self):
        """
        Gets all collections in which the publisher appears via the
        many-to-many table
        """
        return Collection.select().join(
            PublisherInCollection
        ).join(
            Publisher
        ).where(
            Publisher.name == self.name
        )


class Subject(BaseModel):
    name = sql.CharField()

    @property
    def collections(self):
        """
        Gets all collections in which the subject appears via the
        many-to-many table
        """
        return Collection.select().join(
            SubjectInCollection
        ).join(
            Subject
        ).where(
            Subject.name == self.name
        )


class PublisherInCollection(BaseModel):
    """
    The many-to-many table representing each time a publisher was responsible
    for a collection.
    """
    collection = sql.ForeignKey(Collection, related_name='publishers')
    publisher = sql.ForeignKey(Publisher, related_name='collections')


class SubjectInCollection(BaseModel):
    """
    The many-to-many table representing each time a subject appears in a
    collection.
    """
    collection = sql.ForeignKey(Collection, related_name='publishers')
    subject = sql.ForeignKey(Publisher, related_name='collections')
