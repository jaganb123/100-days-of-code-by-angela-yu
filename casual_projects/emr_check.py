import boto3, datetime, re, shelve


class emrObject:
    def __init__(self, name, date) -> None:
        self.pipeline_segment = None
        self.name = name
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.state = None

    def __str__(self) -> str:
        string = f"{self.pipeline_segment}\t{self.name}-{self.date.strftime('%Y-%m-%d')}\t{self.state}"
        return string
    
    def emr_match(self, emrListDict):
        for emr in emrListDict:
            if re.search(self.name, emr['Name']):
                pass
        
pipeline = {
    'data_pipeline' : { 
        'GenerateFilterData-production': '2023-04-19',
        'ImportDedupInfos-production': '2023-04-19', 
        'DataJoinerBidIdFilter-production': '2023-04-19'
        }
    }


emr_list = []
for segment in pipeline.keys():
    for emr in pipeline[segment].keys():
        tmp_obj = emrObject(emr, pipeline[segment][emr])
        tmp_obj.pipeline_segment = segment
        emr_list.append(tmp_obj)
    

