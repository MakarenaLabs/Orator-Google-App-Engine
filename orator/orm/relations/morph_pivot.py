# -*- coding: utf-8 -*-

from .pivot import Pivot


class MorphPivot(Pivot):

    _morph_class = None
    _morph_type = None

    def _set_keys_for_save_query(self, query):
        """
        Set the keys for a save update query.

        :param query: A Builder instance
        :type query: orator.orm.Builder

        :return: The Builder instance
        :rtype: orator.orm.Builder
        """
        query.where(self._morph_type, self._morph_class)

        return super(MorphPivot, self)._set_keys_for_save_query(query)

    def delete(self):
        """
        Delete the pivot model record from the database.

        :rtype: int
        """
        query = self._get_delete_query()

        query.where(self._morph_type, self._morph_class)

        return query.delete()

    def set_morph_type(self, morph_type):
        self._morph_type = morph_type

        return self

    def set_morph_class(self, morph_class):
        self._morph_class = morph_class

        return self
