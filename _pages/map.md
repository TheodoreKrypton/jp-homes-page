---
layout: default
title: Map
permalink: /map
---

<iframe src="https://overpass-turbo.eu/map.html?Q=%5Bout%3Ajson%5D%0A%5Btimeout%3A25%5D%3B%0A%0A%2F%2F+Retrieve+%28surrounding%29+ways+with+amenity%3Dschool%0Away%2849.78968739570404%2C8.46050262451172%2C49.998691591699%2C8.83678436279297%29%5Bamenity%3Dschool%5D%3B%0A%0A%2F%2F+convert+to+area%0Amap_to_area+-%3E.area%3B%0A%0A%28%0A++%2F%2F+Difference+of%3A%0A++%0A++%2F%2F+All+nodes%2Bways+with+building%3Dschool+and+no+amenity%3D*+tag+in+bbox%0A++%28%0A++++node+%5B%22building%22%3D%22school%22%5D%5B%22amenity%22%21%7E%22.%22%5D%2849.78968739570404%2C8.46050262451172%2C49.998691591699%2C8.83678436279297%29%3B%0A++++way%5B%22building%22%3D%22school%22%5D%5B%22amenity%22%21%7E%22.%22%5D%2849.78968739570404%2C8.46050262451172%2C49.998691591699%2C8.83678436279297%29%3B%0A++%29%3B%0A-+%2F%2F+except+for%0A++%28%0A++++%2F%2F+All+nodes%2Bways+with+building%3Dschool+and+no+amenity%3D*+tag+in+area%0A++++node+%5B%22building%22%3D%22school%22%5D%5B%22amenity%22%21%7E%22.%22%5D%28area.area%29%3B%0A++++way%5B%22building%22%3D%22school%22%5D%5B%22amenity%22%21%7E%22.%22%5D%28area.area%29%3B++++%0A++%29%3B%0A%29%3B%0A%0Aout+geom%3B" width="100%" height="500"></iframe>
