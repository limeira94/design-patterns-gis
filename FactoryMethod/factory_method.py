from abc import ABC, abstractmethod


class LoaderFactory(ABC):
    @abstractmethod
    def create_loader(self):
        pass
    

class ShapefileLoaderFactory(LoaderFactory):
    def create_loader(self):
        return ShapefileLoader()
    

class GeoJSONLoaderFactory(LoaderFactory):
    def create_loader(self):
        return GeoJSONLoader()


class Loader(ABC):
    @abstractmethod
    def load(self, filepath):
        pass


class ShapefileLoader(Loader):
    def load(self, filepath):
        print(f'Loading shapefile from {filepath}')
        

class GeoJSONLoader(Loader):
    def load(self, filepath):
        print(f'Loading GeoJSON from {filepath}')


def load_geopastial_data(factory: LoaderFactory, filepath):
    loader = factory.create_loader()
    loader.load(filepath)
    

if __name__ == '__main__':
    filepath = 'path/to/file.shp'
    
    if filepath.endswith('.shp'):
        factory = ShapefileLoaderFactory()
    elif filepath.endswith('.geojson'):
        factory = GeoJSONLoaderFactory()
    else:
        raise ValueError('Unsupported file format')
    
    load_geopastial_data(factory, filepath)
    
