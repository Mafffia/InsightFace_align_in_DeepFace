# InsightFace_align_in_DeepFace
#### Since the align process of deepface is too simple, sometimes naive, we decided to use the alignment from insightface into deepface, but it requies minor change of DeepFace source code, thus we need this repo to maintain the align and the source code.
#### The represent() function in DeepFace does not take align as parameter, thus I modified DeepFace.py in this repository, inorder to use you own align face, you have to turn off the alignment in the DeepFace, to do that, you need to change DeepFace.py in your Python library to the file in this repo.
### Usage
```
  import face_align
  #get the aligned face picture, inputing the file directory
  face_img = face_align.get_face_align(img)
  #you have to turn off detection and align in DeepFace
  arcanalyze = DeepFace.analyze(img_path = face_img, actions = ['age', 'gender', 'race', 'emotion'],detector_backend='skip',align=False)
  #also for getting the embedding of the face
  arcrep = DeepFace.represent(face_img, model_name = 'ArcFace', model = None, enforce_detection = True, detector_backend = 'skip', align = False, normalization = 'base')
 ```
#### If you have more question, please raise an issue.

### Mafffia
