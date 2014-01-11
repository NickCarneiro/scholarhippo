# encapsulates a Scholarship model, includes metadata such as scholarship_key not found in the model
class SerpResult:
    def __init__(self, scholarship_key=None, scholarship_model=None):
        self.scholarship_key = scholarship_key
        self.scholarship_model = scholarship_model
        self.snippet = scholarship_model.description
        if scholarship_model is not None:
            self.deadline = scholarship_model.deadline
        self.source = scholarship_model.organization
        self.href = scholarship_model.third_party_url
        self.title = scholarship_model.title
        self.essay_required = scholarship_model.essay_required
        self.gender_restriction = scholarship_model.gender_restriction
        safe_title = scholarship_model.title[:100].encode('ascii', 'ignore')
        self.vs_href = u'/scholarship/{}?title={}'.format(self.scholarship_key, safe_title)