from django.db.models.manager import Manager


class CoreManager(Manager):
    limit_to = None

    def __init__(self, **kwargs):
        self.limit_to = kwargs
        super(CoreManager, self).__init__()

    def get_queryset(self):
        if self.limit_to:
            return super().get_queryset().filter(**self.limit_to)
        return super().get_queryset()
