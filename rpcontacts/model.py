# -*- coding: utf-8 -*-

"""Этот модуль предоставляет модель для управления таблицей контактов."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Создание и настройка модели"""
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
        """Добавление контактов в базу данных"""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()

    def FindContact(self, data):
        """Поиск контактов в базе данных"""
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            pass

    def deleteContact(self, row):
        """Удаление контактов с базы данных"""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearContacts(self):
        """Удалить все контакты с базы данных"""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
