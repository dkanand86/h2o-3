from ..estimators.estimator_base import H2OEstimator


class H2OPCA(H2OEstimator):
  """
  Principal Component Analysis
  """

  def __init__(self, model_id=None, k=None, max_iterations=None, seed=None,
               transform=("NONE","DEMEAN","DESCALE","STANDARDIZE","NORMALIZE"),
               use_all_factor_levels=False,
               pca_method=("GramSVD", "Power", "GLRM")):
    """
    Principal Components Analysis

    Parameters
    ----------
      model_id : str, optional
        The unique hex key assigned to the resulting model. Automatically generated if
        none is provided.
      k : int
        The number of principal components to be computed. This must be between 1 and
        min(ncol(training_frame), nrow(training_frame)) inclusive.
      transform : str
        A character string that indicates how the training data should be transformed
        before running PCA. Possible values are
          "NONE": for no transformation,
          "DEMEAN": for subtracting the mean of each column,
          "DESCALE": for dividing by the standard deviation of each column,
          "STANDARDIZE": for demeaning and descaling, and
          "NORMALIZE": for demeaning and dividing each column by its range (max - min).
      seed : int, optional
         Random seed used to initialize the right singular vectors at the beginning of
         each power method iteration.
      max_iterations : int, optional
        The maximum number of iterations when pca_method is "Power"
      use_all_factor_levels : bool, optional
        A logical value indicating whether all factor levels should be included in each
        categorical column expansion. If False, the indicator column corresponding to the
        first factor level of every categorical variable will be dropped. Default False.
      pca_method : str
        A character string that indicates how PCA should be calculated. Possible values
        are
          "GramSVD": distributed computation of the Gram matrix followed by a local SVD
          using the JAMA package,
          "Power": computation of the SVD using the power iteration method,
          "GLRM": fit a generalized low rank model with an l2 loss function
          (no regularization) and solve for the SVD using local matrix algebra.

    Returns
    -------
      A new instance of H2OPCA.
    """
    super(H2OPCA, self).__init__()
    self.parms = locals()
    self.parms = {k: v for k, v in self.parms.iteritems() if k != "self"}
    self.parms["pca_method"] = "GramSVD" if isinstance(pca_method, tuple) else pca_method
    self.parms["transform"] = "NONE" if isinstance(transform, tuple) else transform
    self.parms["algo"] = "pca"

  def fit(self, X,y=None,  **params):
    return super(H2OPCA, self).fit(X)

  def transform(self, X, y=None, **params):
    """
    Transform the given H2OFrame with the fitted PCA model.

    Parameters
    ----------
      X : H2OFrame
        May contain NAs and/or categorical data.
      y : H2OFrame
        Ignored for PCA. Should be None.
      params : dict
        Ignored.

    Returns
    -------
      The input H2OFrame transformed by the Principal Components
    """
    return self.predict(X)