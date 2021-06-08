class FieldLookUpMixin:
    def get_queryset(self):
        queryset = self.queryset
        lookup_filter = {}

        for lookup_field in self.lookup_fields:
            if self.request.data.get(lookup_field):
                lookup_filter[f"{lookup_field}__icontains"] = self.request.data.get(
                    lookup_field
                )

        queryset = queryset.filter(**lookup_filter)

        return queryset
