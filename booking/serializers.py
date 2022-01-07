from rest_framework import serializers 

class RoomFacilitySerializer(serializers.BaseSerializer):
    def to_representation(self,instance):
        return{
            "cod_facility":instance.cod_facility,
            "facility":instance.facility,
        }

class RoomSerializer(serializers.BaseSerializer):

    def to_representation(self,instance):
        
        serializer_facilities = RoomFacilitySerializer(instance.facilities.all(), many=True)
        return {
            "id":instance.id,
            "title":instance.title,
            "description" : instance.description,
            "guests": instance.guests,
            "beds": instance.beds,
            "toilets": instance.toilets,
            "cost_per_night" :instance.cost_per_night,
            "facilities":serializer_facilities.data
        }