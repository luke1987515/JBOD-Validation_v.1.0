"""
validation/services.py

Business Logic Layer

所有 Validation 商業邏輯集中在這裡。

View 不直接存資料庫，
而是呼叫 Service。
"""

from django.db import transaction

from .models import Validation


class ValidationService:
    """
    Validation Service
    """

    @staticmethod
    @transaction.atomic
    def create_validation(form):
        """
        建立 Validation

        Parameters
        ----------
        form : ValidationForm
            已經通過 is_valid() 的 Form

        Returns
        -------
        Validation
        """

        validation = form.save()

        #
        # 未來可以加入：
        #
        # 建立 Working Directory
        #
        # 建立 Report Folder
        #
        # 建立 Log Folder
        #
        # 建立 Execution Queue
        #
        # 初始化 Test Result
        #

        return validation