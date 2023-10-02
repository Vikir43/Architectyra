from abc import ABC, abstractmethod
from typing import List

from model_store import Flash, Camera, Scene, PolygonalModel


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self) -> None:
        pass


class ModelStore(IModelChanger, ABC):
    def __init__(self, change_observers: List[IModelChangedObserver]):
        self.__change_observers = change_observers
        self.models = list()
        self.scenes = list()
        self.flashes = list()
        self.cameras = list()

        self.models.append(PolygonalModel())
        self.scenes.append(Scene(1, self.models, self.flashes, self.cameras))
        self.flashes.append(Flash())
        self.cameras.append(Camera())

    models: List[PolygonalModel]
    scenes: List[Scene]
    flashes: List[Flash]
    cameras: List[Camera]
    __change_observers: List[IModelChangedObserver]

  
    def notify_change(self) -> None:
        pass

    def get_scene(self, id_num: int) -> Scene | None:
        for scene in self.scenes:
            if scene.id == id_num:
                return scene
        return None