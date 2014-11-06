from django.contrib import admin

from models import *

admin.site.register(Country)
admin.site.register(Patient)
admin.site.register(AdditionalProcedure)
admin.site.register(AnaestheticType)
admin.site.register(Complication)
admin.site.register(DifficultyFactor)
admin.site.register(Eye)
admin.site.register(Gender)
admin.site.register(IolPosition)
admin.site.register(KeratomyUnit)
admin.site.register(OcularCopathology)
admin.site.register(PostOpComplication)
admin.site.register(RefractionType)
admin.site.register(SurgeonGrade)
admin.site.register(SurgeryReason)
admin.site.register(VisualAcuityCorrection)
admin.site.register(VisualAcuityScale)

class PreOpAssessmentVisualAcuityReadingInline(admin.TabularInline):
    model = PreOpAssessmentVisualAcuityReading

class PreOpAssessmentAdmin(admin.ModelAdmin):
    inlines = [
        PreOpAssessmentVisualAcuityReadingInline,
    ]

admin.site.register(PreOpAssessment, PreOpAssessmentAdmin)
