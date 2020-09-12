![logo](http://i.imgur.com/lVMTcfS.png)


YABEE 15.2
=====
Renewed Egg exporter for Blender 2.8 and Panda3D

Exporting:
- Meshes
- UV layers
- Materials 
- Vertex colors
- Textures (Diffuse, Normal, Roughness)
- Armature (skeleton) animations
- ShapeKeys (morph) animation
- Non-cyclic NURBS Curves

New minor features
=====
- Automatic selection
- Apply object transform
- Set texture format to RGB or RGBA (with saving it to .bam file in /tmp directory)

**These features activated by default**, uncheck them first if you don't use them and manually select your object(s).
**Automatic selection** automatically selects all objects in the scene. 
**Apply object transform** will change **only copy** of the scene prepared for an export.

Missing features/TODO
=====
- Properties/tags
- Texture baking via Cycles
- Blender Lights

Principled Shader Support
=====
With the addition of the the Principled BSDF shader in Blender and the upcomming support for physically based materials 
in Panda3D it was possible to extend YABEE to improve the workflow for artists when working in a PBR environment. 

<img src="https://i.imgur.com/v37q51J.png" />
<p style="font-size: small">YABEE becomes more Blender-compatible: No special Nodegroup is needed anymore</p>

<img src="https://i.imgur.com/7hEFhqr.png" />
<p style="font-size: small">Normal mapping Setup for Panda3D (with TBS option)</p>

<img src="https://i.imgur.com/lndfqdr.jpg" />
<p style="font-size: small">Normal mapping Setup for Panda3D + RenderPipeline (with TBS option)</p>

To use it, you have to create a material for your mesh, set up the Principled BSDF shader 
by connecting at least the Image Texture shader and optionally UV Map.

The PBR node support is still work in progress, if you find important features missing please contact the developers.

**Use this version of YABEE carefully. It doesn't support previous Blender 2.7 versions. It may contain bugs and may not work for objects with complex node system 
applied (something more than UVMap and Texture Image).**

1. **Do backup** of your blend files first or revert the project after exporting.
2. To avoid further issues, don't save your project after export is done. Save it **BEFORE** exporting.

How To Export
=====
Before exporting:

<img src="https://i.imgur.com/8bjCJ8z.jpg" />

1. Select all meshes of the character except armature, or
2. Select all meshes of the character including armature
