# README.md

# Project: Synthetic Dataset Construction with 3D Simulation in Blender

## Description
This project aims to develop a synthetic dataset using a 3D digital environment to complement the training images of semantic segmentation models. The focus is to faithfully replicate the characteristics of the real environment, including variations in lighting and different adverse conditions, using Blender as the main tool.



![10](https://github.com/fridriscvski/blender_digital_twin/assets/117530891/664f542a-9112-4412-869b-552b1362156a)
## Methodology
### 1. Modeling Plant Leaves
Modeling the leaves of weed plants is crucial to ensure that the generated images resemble real ones. The process involves:
- Separating leaves of each weed species and capturing the images in PNG format, without a background.
- Converting the images to contours in SVG format.
- Inserting the contours into Blender to create 3D molds (Meshes) with contour and shadow characteristics.
- Adding textures using normal maps generated in GIMP to simulate depth and light reflections.

### 2. Plant Structure
The structure of the plants is modeled in Blender using Geometry Nodes to create and manipulate geometry procedurally. This allows for:
- Variation of parameters such as height, stem diameter, number of leaves, and leaf spacing.

### 3. Lighting and Shading
Using HDRIs (High Dynamic Range Images) to create realistic lighting in the 3D environment. These HDRIs are extracted from the Poly Haven platform and are essential for:
- Capturing a diverse range of environments and lighting conditions.

### 4. Simulation
The simulation involves creating complete scenarios that include structures, weeds, and textures, using Blender's Cycles renderer, which offers:
- High-quality results based on ray tracing, calculating light propagation and generating realistic reflections and shadows.
- Using embedded Python scripts in Blender to automate and optimize the rendering of a large number of images, varying parameters such as the number and variety of plants and lighting scenarios.

### 5. Mask Creation
For training the semantic segmentation models, it is necessary to create masks corresponding to the simulated images. This process includes:
- Additional renderings to capture detailed information of the different weed species.
- Generating accurate and diverse masks for effective training of the models.

## Tools Used
- **Blender**: Main tool for 3D modeling and simulation.
- **GIMP**: Used to generate normal maps for the leaf textures.
- **Python**: For automating and optimizing the rendering process in Blender.

## Usage Instructions

1. **Preparing the Leaves**:
   - Capture images of weed leaves in PNG format, without a background.
   - Convert these images to SVG format using image editing tools.

2. **Blender Configuration**:
   - Load the converted images into Blender to create 3D meshes.
   - Add textures to the meshes using normal maps generated in GIMP.

3. **Modeling Plant Structures**:
   - Use Geometry Nodes in Blender to create procedural plant structures.

4. **Lighting Configuration**:
   - Import HDRIs from the Poly Haven platform to set up lighting in Blender.

5. **Simulation and Rendering**:
   - Use Python scripts to automate and optimize the rendering process in Blender.
   - Render various scenarios, adjusting parameters as necessary.

6. **Mask Creation**:
   - Perform additional renderings to capture detailed information of the weed plants.
   - Generate accurate masks for training semantic segmentation models.

