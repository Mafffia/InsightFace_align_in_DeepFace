# InsightFace_align_in_DeepFace
#### Since the align process of deepface is too simple, sometimes naive, we decided to use the alignment from insightface into deepface, but it requies minor change of DeepFace source code, thus we need this repo to maintain the align and the source code.
#### The represent() function in DeepFace does not take align as parameter, thus I modified DeepFace.py in this repository, inorder to use you own align face, you have to turn off the alignment in the DeepFace, to do that, you only need to import my DeepFace.py.
### Install requirements
```
  pip install -r requirements.txt
```
### import face align and get aligned face
```
  import face_align
  face_aligned = face_align.get_face_align(img_file)
 ```
 ### import modified deepface
```
  import DeepFace
  #Turning off align in deepface, also remember to turn off detector.
  #analyze face
  arcanalyze = DeepFace.analyze(face_aligned, actions = ['age', 'gender', 'race', 'emotion'],detector_backend='skip',align=False)
  #face embedding(512*1 dim)
  arcrep = DeepFace.represent(face_aligned, model_name = 'ArcFace', model = None, enforce_detection = True, detector_backend = 'skip', align = False, normalization = 'base')
 ```

#### In test_align.ipynb, I made an demo showing difference between face align in insightface and deepface.

#### If you have more question, please raise an issue.

### Mafffia
