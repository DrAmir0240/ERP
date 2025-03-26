from rest_framework import serializers
from .models import Cargo, CargoImage
from Storage.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CargoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoImage
        fields = ['id', 'image', 'uploaded_at']


class CargoSerializer(serializers.ModelSerializer):
    images = CargoImageSerializer(many=True, required=False)  # سریالایزر برای لیست تصاویر
    cargo_id = serializers.CharField(read_only=True)  # به‌صورت خودکار مقداردهی می‌شود

    class Meta:
        model = Cargo
        fields = [
            'id', 'cargo_id', 'name', 'category', 'owner', 'manager',
            'weight', 'value', 'date_added', 'images'
        ]

    def create(self, validated_data):
        """ساخت Cargo همراه با تصاویر"""
        images_data = self.context['request'].FILES.getlist('images')  # دریافت لیست تصاویر
        cargo = Cargo.objects.create(**validated_data)  # ایجاد Cargo
        cargo.cargo_id = cargo.generate_cargo_id()  # مقداردهی `cargo_id`
        cargo.save()

        # ایجاد تصاویر مرتبط
        for image_data in images_data:
            CargoImage.objects.create(cargo=cargo, image=image_data)

        return cargo
