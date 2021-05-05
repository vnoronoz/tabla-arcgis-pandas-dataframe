import arcpy
import pandas as pd

def table_to_data_frame(in_table, input_fields=None, where_clause=None):
    """
	Convierte una tabla ArcGIS en un dataframe de Pandas con un índice de ID de objeto, y los
    campos de entrada seleccionados.
	"""
    OIDFieldName = arcpy.Describe(in_table).OIDFieldName
    if input_fields:
        final_fields = [OIDFieldName] + input_fields
    else:
        final_fields = [field.name for field in arcpy.ListFields(in_table)]
    data = [row for row in arcpy.da.SearchCursor(in_table, final_fields, where_clause=where_clause)]
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
    
    return fc_dataframe
