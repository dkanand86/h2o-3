import sys, os

sys.path.insert(1, "../../../")
import h2o
from tests import pyunit_utils
from h2o.estimators.isolation_forest import H2OIsolationForestEstimator

def gbm_mojo_reproducibility_info():
    prostate_hex = h2o.import_file(pyunit_utils.locate("smalldata/testng/prostate.csv"))

    model = H2OIsolationForestEstimator()
    model.train(training_frame=prostate_hex)

    print("Downloading Java prediction model code from H2O")
    TMPDIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath('__file__')), "..", "results", model._id))
    os.makedirs(TMPDIR)
    mojo_path = model.download_mojo(path=TMPDIR)
    gbmModel = h2o.upload_mojo(mojo_path=mojo_path)

    isinstance(gbmModel._model_json['output']['reproducibility_information_map']['cluster configuration']['H2O cluster uptime'], int)
    isinstance(gbmModel._model_json['output']['reproducibility_information_map']['node information']['Node 0']['java_version'], str)
    isinstance(gbmModel._model_json['output']['reproducibility_information_map']['input frames information']['training_frame_checksum'], int)


if __name__ == "__main__":
    pyunit_utils.standalone_test(gbm_mojo_reproducibility_info)
else:
    gbm_mojo_reproducibility_info()
