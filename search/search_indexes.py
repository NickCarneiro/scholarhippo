from haystack import indexes
from search.models import Scholarship


class ScholarshipIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    state_restriction = indexes.CharField(model_attr='state_restriction')
    deadline = indexes.DateField(model_attr='deadline', null=True)
    deadline2 = indexes.DateField(model_attr='deadline2', null=True)
    deadline3 = indexes.DateField(model_attr='deadline3', null=True)
    gender_restriction = indexes.IntegerField(model_attr='gender_restriction', null=True)
    sponsored = indexes.BooleanField(model_attr='sponsored')
    ethnicity_restriction = indexes.IntegerField(model_attr='ethnicity_restriction', null=True)
    essay_required = indexes.BooleanField(model_attr='essay_required')

    def get_model(self):
        return Scholarship

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # only index unexpired scholarships
        return self.get_model().objects.filter(status=0)