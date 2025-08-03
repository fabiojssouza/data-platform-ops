{{/* Expand the name of the chart. */}}
{{- define "app-of-apps.name" -}}
{{- default.Chart.Name.Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}