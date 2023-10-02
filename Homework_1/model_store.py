from typing import List

from service import Angle3D, Color, Point3D


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, angle: Angle3D) -> None: pass

    def move(self, location: Point3D) -> None: pass


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle: Angle3D) -> None: pass

    def move(self, location: Point3D) -> None: pass


class Polygon:
    def __init__(self, points: List[Point3D]):
        self.points = points

    points: List[Point3D] = list()


class Texture:
    pass


class PolygonalModel:
    def __init__(self, textures: List[Texture] = None):
        self.polygons = list()
        self.textures = textures

    polygons: List[Polygon]
    textures: List[Texture]

class Scene:
    def __init__(self, id_num: int, models: List[PolygonalModel], flashes: List[Flash], cameras: List[Camera]):
        self.id = id_num

        if not models:
            raise Exception('Добавьте модель')
        else:
            self.models = models

        self.flashes = flashes

        if not cameras:
            raise Exception('Добавьте камеру')
        else:
            self.cameras = cameras

    id: int
    models: List[PolygonalModel]
    flashes: List[Flash]
    cameras: List[Camera]


    def method1(self, type_value: type) -> type:
        result: type = None
        return result


    def method2(self, type_value1: type, type_value2: type) -> type:
        result: type = None
        return result