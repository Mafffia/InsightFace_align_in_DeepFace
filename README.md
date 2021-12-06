# InsightFace_align_in_DeepFace
#### By looking into the align process of deepface, we found it using simple method so that sometimes it cannot handle face detection & alignment, thus we tried to use the alignment from InsightFace and replace it into DeepFace. It only requries minor change of DeepFace source code, and we need this repo to maintain the alignment and the source code.
#### The represent() function in DeepFace does not take alignment as parameter, thus the modified DeepFace.py was proposed in this repository. You can use your own faces for testing by setting the alignment argument to False in DeepFace and importing modified DeepFace.py.
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
