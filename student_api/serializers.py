from rest_framework import serializers
from .models import Path, Student
from django.utils.timezone import now


# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     id = serializers.IntegerField(required=False)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ["first_name", "last_name", "number", "days_since_joined"]


    def validate_first_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Isminiz 3 karakterden kucuk olamaz")
        return value

    def validate_number(self, value):
        if value < 10:
            raise serializers.ValidationError("This is not a valid number")
        return value

    def validate(self, data):
        """
        iki value karşılaştırma
        """
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError("ad soyad aynı olamaz")
        return data

    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).seconds
        # exclude = ('id',) 
        # depth = 1
        # many = True
        # read_only_fields = ('id',)
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True},
        #     'number': {'required': True},
        # }
        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=Student.objects.all(),
        #         fields=('first_name', 'last_name')
        #     )
        # ]
   
class PathSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True, read_only=True) #*tüm bilgiler gelir
    #student = serializers.StringRelatedField(many=True) #* modelde yapılan str methodu görünür.
    # student = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #* modelde yapılan path_name field ve id gösterir
    class Meta:
        model = Path
        fields = "__all__"