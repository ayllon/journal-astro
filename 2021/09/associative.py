from typing import List, Tuple

import numpy as np


class AssociativeArray:
    NOT_SET = 0x00
    SET = 0x01

    def __init__(self, references: np.ndarray, n_sources: int, n_neighbors: int,
                 fields: List[Tuple[str, np.dtype]] = None):
        dtype = [('object_id', np.int64), ('next', np.int32), ('flag', np.int8)]
        self._field_names = ['object_id']
        if fields:
            dtype.extend(fields)
            self._field_names.extend([f[0] for f in fields])
        self._n_sources = n_sources
        self._n_neighbors = n_neighbors
        self._ref_index = np.full(
            len(references), -1,
            dtype=[('reference_id', np.int64), ('first', np.int32), ('last', np.int32)]
        )
        self._ref_index['reference_id'] = references
        self._ref_index['reference_id'].sort()
        self._data = np.zeros(self._n_sources * self._n_neighbors, dtype=dtype)
        self._data['next'] = -1
        self._next_free = 0

    def _get_index(self, ref_id: int):
        offset = self._ref_index['reference_id'].searchsorted(ref_id)
        index = self._ref_index[offset]
        if ref_id != index['reference_id']:
            raise KeyError(ref_id)
        return index

    def get(self, ref_id: int):
        index = self._get_index(ref_id)
        result = list()
        next = index['first']
        while next > -1:
            record = self._data[next]
            result.append(record[self._field_names])
            next = record['next']
        return np.array(result)

    def _find_next_free(self, offset):
        next_free = self._next_free
        self._next_free += 1
        return next_free

    def _find_free(self, hint):
        if hint['last'] > -1:
            return self._find_next_free(hint['last'])
        return self._find_next_free(hint['reference_id'] // 10)

    def append(self, ref_id: int, source_id: int, **kwargs):
        index = self._get_index(ref_id)
        insert_pos = self._find_free(index)

        new_record = self._data[insert_pos]
        new_record['flag'] = self.SET
        new_record['object_id'] = source_id
        for k, v in kwargs.items():
            new_record[k] = v

        if index['last'] > -1:
            self._data[index['last']]['next'] = insert_pos
        index['last'] = insert_pos
        if index['first'] < 0:
            index['first'] = index['last']

    def __iter__(self):
        for index in self._ref_index:
            if index['first'] > -1:
                yield index['reference_id']
